##########################################
#   ___ __  __ ___  ___  ___ _____ ___   #
#  |_ _|  \/  | _ \/ _ \| _ |_   _/ __|  #
#   | || |\/| |  _| (_) |   / | | \__ \  #
#  |___|_|  |_|_|  \___/|_|_\ |_| |___/  #
#                                        #
##########################################


from pandas import DataFrame
import pandas as pd
from datetime import date

import numpy as np
import matplotlib.pyplot as plt
import missingno as msno

from typing import Any
from pathlib import Path
from config import DATA_DIR

import seaborn as sns

#############################################
#   ___ _____ _   _  _ ___   _   ___ ___    #
#  / __|_   _/_\ | \| |   \ /_\ | _ |   \   #
#  \__ \ | |/ _ \| .` | |) / _ \|   | |) |  #
#  |___/ |_/_/ \_|_|\_|___/_/ \_|_|_|___/   #
#                                           #
#############################################

TODAY = date.today()
DATE_FORMAT = str(TODAY.year) + str(TODAY.month) + str(TODAY.day)

# Turn interactive plotting off
plt.ioff()

#########################################################
#   ___  ___ ___ ___ _  _ ___ _____ ___ ___  _  _ ___   #
#  |   \| __| __|_ _| \| |_ _|_   _|_ _/ _ \| \| / __|  #
#  | |) | _|| _| | || .` || |  | |  | | (_) | .` \__ \  #
#  |___/|___|_| |___|_|\_|___| |_| |___\___/|_|\_|___/  #
#                                                       #
#########################################################

        
class EvaluateDataset:
    """ Standard evaluation and visualization for the dataframe. """
    def __init__(
            self, 
            input_df:DataFrame, 
            data_name:str, 
            
            export_plot:bool=False, 
            show_plot:bool=False,
            
            output_path:Path = DATA_DIR,
        ) -> None:
        
        self.df:DataFrame = input_df
        self.name:str = data_name.title()
        #self._profile = ProfileReport(self.df, title=self.name)
        
        self._export = export_plot
        self._show = show_plot
        
        self._color = "orange"
        self._figsize = (16,10) 
        self._dpi = 720
        self._aspect = 3
        
        self.output_path = output_path
        plt.ioff()
        
    @property
    def dataframe(self):
        return self.df
        
    @property
    def profile(self):
        return self._profile
            
    # def get_profiling(self) -> None:
    #     profile_name = f"{DATE_FORMAT}-{self.name}Data_Profiling.html"
    #     if self._export:
    #         self._profile.to_file(self.output_path / profile_name)
        
    def get_all_corr(self, show:bool=False):
        all_correlation = ["spearman", "kendall", "pearson"]
    
        for corr in all_correlation:
            plt.figure(figsize=self._figsize, dpi=self._dpi)
            df_corr = self.df.corr(method=corr)
            
            fig = sns.heatmap(df_corr, annot=True, cmap="inferno", center=0)
            fig.set(title=f"{self.name} - {corr.title()} Correlation Heatmap")
            
            fig_name = f"{DATE_FORMAT}-{self.name}Data_Corr{corr.title()}.png"
            self._saving_and_showing(_name = fig_name, _show = show)
    
    def get_all_hist(self, show:bool=False):
        num_in_df = self.df.select_dtypes(include="number")
        row_size = math.ceil(len(num_in_df.columns) / 4) * 5
        fig = num_in_df.hist(bins=20, color=self._color, figsize=(30, row_size))
        
        fig_name = f"{DATE_FORMAT}-{self.name}Data_Hist.png"
        self._saving_and_showing(_name = fig_name, _show = show)

        
    def get_category_hist(self, column_name:str, show:bool=False):
        fig = sns.displot(self.df[column_name], discrete=True, aspect=self._aspect, kind='hist', color=self._color)
        
        # Setting the x label
        xlabel = column_name.replace("_", " ").title()
        
        # Setting the title
        title_name = f"{self.name.title()} Data - Count over {column_name.title()}"
        fig.set(title=title_name, xlabel=xlabel)
        fig.tight_layout()
        
        fig_name = f"{DATE_FORMAT}-{self.name}Data_{column_name.title()}_CategoryHist.png"
        self._saving_and_showing(_name = fig_name, _show = show)
        
    def _saving_and_showing(self, _name:str, _show:bool):
        if self._export:
            plt.savefig(self.output_path / _name)
        
        # Show or Hide Plot
        if self._show or _show:
            plt.show()
        else:
            plt.close("all")
        
        

class CountMissingData:
    """ Get the missing data count and percentage based on input dataframe. """
    
    def __init__(self, input_df:DataFrame) -> DataFrame:
        self.df = input_df
        
    def get(self):
        total = self.df.isnull().sum().sort_values(ascending=False)
        percent = (self.df.isnull().sum()/self.df.isnull().count()).sort_values(ascending=False)
        missing_data = pd.concat([total, percent], axis=1, keys=['Missing_Count', 'Missing_Percent%'])
        return missing_data
        
        

class VisualizeMissing:
    def __init__(
            self, 
            input_df:DataFrame, 
            name:str, 
            
            export_plot:bool=False, 
            show_plot:bool=False,
            
            process_null:bool=False, 
            process_zero:bool=False,
            
            output_path = DATA_DIR
        ) -> None:
        
        self.df:DataFrame = input_df
        self._process_data(replace_null=process_null, replace_zero=process_zero)
        self.name = name.title()
        
        self._export = export_plot
        self._show = show_plot
        
        self._fontsize:int = 16
        self._label_rotation:int = 90
        self._figsize:int = (30,15)
        
        self.output_path:Path = output_path
        
        self._about:str = "Visualize Missing, NA, 0 values"
        plt.ioff()
        
        
    def _process_data(self, replace_null:bool, replace_zero:bool):
        """ Process the dataframe. """
        if replace_null:
            self.df.replace("", np.NaN, inplace=True)
        if replace_zero:
            self.df.replace(0,  np.NaN, inplace=True)
            
    def _saving_and_showing(self, _name:str, _show:bool) -> Any:
        if self._export:
            plt.savefig(self.output_path / _name)
        
        # Show or Hide Plot
        if self._show or _show:
            plt.show()
        else:
            plt.close("all")
        
    def Bar(self, show:bool=False):
        fig = msno.bar(
            df = self.df, 
            fontsize = self._fontsize,
            label_rotation = self._label_rotation,
            figsize = self._figsize
        )
        
        chart_name = f"{self.name} Data - Bar Chart - {self._about}"
        fig_name = f"{DATE_FORMAT}-{self.name}Data_BarChart-NullExplore.png"
        fig.set(title=chart_name)
        
        # Save or Show the results
        self._saving_and_showing(_name = fig_name, _show = show)
    
    def Matrix(self, show:bool=False):
        fig = msno.matrix(
            df = self.df, 
            fontsize = self._fontsize,
            label_rotation = self._label_rotation,
            figsize = self._figsize
        )
        
        chart_name = f"{self.name} Data - Matrix Chart - {self._about}"
        fig_name = f"{DATE_FORMAT}-{self.name}Data_MatrixChart-NullExplore.png"
        fig.set(title=chart_name)
        
        # Save or Show the results
        self._saving_and_showing(_name = fig_name, _show = show)
    
    def Heatmap(self, show:bool=False):
        fig = msno.heatmap(
            df = self.df, 
            fontsize = self._fontsize,
            label_rotation = self._label_rotation,
            figsize = self._figsize
        )
        
        chart_name = f"{self.name} Data - Heatmap Chart - {self._about}"
        fig_name = f"{DATE_FORMAT}-{self.name}Data_HeatmapChart-NullExplore.png"
        fig.set(title=chart_name)
        
        # Save or Show the results
        self._saving_and_showing(_name = fig_name, _show = show)
    

######################################
#   ___ ___  ___   ___ ___ ___ ___   #
#  | _ | _ \/ _ \ / __| __/ __/ __|  # 
#  |  _|   | (_) | (__| _|\__ \__ \  #
#  |_| |_|_\\___/ \___|___|___|___/  #
#                                    #
######################################

if __name__ == "__main__":
    None